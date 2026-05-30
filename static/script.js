async function predict() {

    const hours = document.getElementById("hours").value;
    const score = document.getElementById("score").value;

    const response = await fetch("http://127.0.0.1:8000/predict", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({
            hours_studied: parseFloat(hours),
            exam_score: parseFloat(score)
        })
    });

    const data = await response.json();

    document.getElementById("result").innerText =
        data.result === 1 ? "PASS ✅" : "FAIL ❌";
}