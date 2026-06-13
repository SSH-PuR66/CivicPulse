async function loadDashboard() {
    const status = document.getElementById("status");
    try {
        const res = await fetch("/api/states");
        if (!res.ok) throw new Error(`HTTP ${res.status}`);
        const { states } = await res.json();
        status.textContent = `Loaded ${states.length} states.`;
        renderChart("popChart", states, "population", "#1f6feb", "Population");
        renderChart("incomeChart", states, "median_income", "#2da44e", "Median income (USD)");
        renderTable(states);
    } catch (err) {
        status.textContent = "Failed to load data. Please try again later.";
        console.error(err);
    }
}

function renderChart(canvasId, states, field, color, label) {
    const top = [...states]
        .filter((s) => s[field] != null)
        .sort((a, b) => b[field] - a[field])
        .slice(0, 15);

    new Chart(document.getElementById(canvasId), {
        type: "bar",
        data: {
            labels: top.map((s) => s.name),
            datasets: [{ label, data: top.map((s) => s[field]), backgroundColor: color }],
        },
        options: {
            indexAxis: "y",
            plugins: { legend: { display: false } },
            scales: { x: { ticks: { callback: (v) => v.toLocaleString() } } },
        },
    });
}

function renderTable(states) {
    const tbody = document.querySelector("#dataTable tbody");
    const fmt = (v) => (v == null ? "—" : v.toLocaleString("en-US"));
    tbody.innerHTML = states
        .map(
            (s) =>
                `<tr><th scope="row">${s.name}</th><td>${fmt(s.population)}</td><td>${fmt(s.median_income)}</td></tr>`
        )
        .join("");
}

loadDashboard();
