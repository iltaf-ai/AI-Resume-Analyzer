const token = localStorage.getItem("token");

if (!token) {
    window.location.href = "/login";
}

const score = document.getElementById("score");
const skills = document.getElementById("skills");
const strengths = document.getElementById("strengths");
const weaknesses = document.getElementById("weaknesses");
const suggestions = document.getElementById("suggestions");
const roadmap = document.getElementById("roadmap");
const logoutBtn = document.getElementById("logoutBtn");


function formatText(text) {

    if (!text) {
        return "No information available.";
    }

    return text
        .replace(/\\#/g, "#")
        .replace(/\\\*/g, "*")
        .replace(/\n/g, "<br>")
        .replace(/\*\*(.*?)\*\*/g, "<strong>$1</strong>")
        .replace(/### (.*?)(<br>|$)/g, "<h3>$1</h3>")
        .replace(/- (.*?)(<br>|$)/g, "• $1<br>");
}


async function getAnalysis() {

    try {

        const response = await fetch("/analysis/data", {
            method: "GET",
            headers: {
                "Authorization": "Bearer " + token
            }
        });


        const data = await response.json();

        console.log("STATUS:", response.status);
        console.log("DATA:", data);


        if (response.status === 401) {

            localStorage.removeItem("token");
            window.location.href = "/login";

            return;
        }


        if (!response.ok) {

            throw new Error(
                data.detail || "Failed to load analysis"
            );

        }


        const analysis = data.analysis || "";


        console.log("ANALYSIS:", analysis);


        // SCORE

        const scoreMatch = analysis.match(
            /Resume Score:\s*\**(\d+)\s*\/\s*100/i
        );


        if (scoreMatch) {

            score.textContent = scoreMatch[1];

        } else {

            score.textContent = "--";

        }


        // SECTION POSITIONS

        const skillsStart = analysis.search(
            /##\s*2\.\s*Skills/i
        );

        const strengthsStart = analysis.search(
            /##\s*3\.\s*Strengths/i
        );

        const weaknessesStart = analysis.search(
            /##\s*4\.\s*Weaknesses/i
        );

        const suggestionsStart = analysis.search(
            /##\s*5\.\s*Improvement Suggestions/i
        );

        const roadmapStart = analysis.search(
            /##\s*6\.\s*Career Roadmap/i
        );


        console.log("Skills:", skillsStart);
        console.log("Strengths:", strengthsStart);
        console.log("Weaknesses:", weaknessesStart);
        console.log("Suggestions:", suggestionsStart);
        console.log("Roadmap:", roadmapStart);


        // SKILLS

        if (
            skillsStart !== -1 &&
            strengthsStart !== -1
        ) {

            skills.innerHTML = formatText(
                analysis.substring(
                    skillsStart,
                    strengthsStart
                )
            );

        } else {

            skills.textContent = "No skills found.";

        }


        // STRENGTHS

        if (
            strengthsStart !== -1 &&
            weaknessesStart !== -1
        ) {

            strengths.innerHTML = formatText(
                analysis.substring(
                    strengthsStart,
                    weaknessesStart
                )
            );

        } else {

            strengths.textContent = "No strengths found.";

        }


        // WEAKNESSES

        if (
            weaknessesStart !== -1 &&
            suggestionsStart !== -1
        ) {

            weaknesses.innerHTML = formatText(
                analysis.substring(
                    weaknessesStart,
                    suggestionsStart
                )
            );

        } else {

            weaknesses.textContent = "No weaknesses found.";

        }


        // SUGGESTIONS

        if (
            suggestionsStart !== -1 &&
            roadmapStart !== -1
        ) {

            suggestions.innerHTML = formatText(
                analysis.substring(
                    suggestionsStart,
                    roadmapStart
                )
            );

        } else {

            suggestions.textContent = "No suggestions found.";

        }


        // ROADMAP

        if (roadmapStart !== -1) {

            roadmap.innerHTML = formatText(
                analysis.substring(
                    roadmapStart
                )
            );

        } else {

            roadmap.textContent = "No roadmap found.";

        }

    }


    catch (error) {

        console.error("Analysis Error:", error);

        score.textContent = "--";

        skills.textContent =
            "Unable to load analysis.";

        strengths.textContent = "";

        weaknesses.textContent = "";

        suggestions.textContent = "";

        roadmap.textContent = "";

    }

}


getAnalysis();


if (logoutBtn) {

    logoutBtn.addEventListener(
        "click",
        function () {

            localStorage.removeItem("token");

            window.location.href = "/login";

        }
    );

}