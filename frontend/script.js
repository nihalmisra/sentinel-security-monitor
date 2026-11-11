
const API_URL = "http://127.0.0.1:8001";

// Load security events
async function loadEvents() {
    try {
        const response = await fetch(`${API_URL}/events`);
        if (!response.ok) throw new Error("Events request failed");

        const events = await response.json();

        document.getElementById("total-events").textContent =
            events.length;

    } catch (error) {
        console.error("Events error:", error);
    }
}

// Load security alerts
async function loadAlerts() {
    try {
        const response = await fetch(`${API_URL}/alerts`);
        if (!response.ok) throw new Error("Alerts request failed");

        const alerts = await response.json();

        document.getElementById("total-alerts").textContent =
            alerts.length;

        document.getElementById("high-alerts").textContent =
            alerts.filter(a => a.severity === "HIGH").length;

        const alertList = document.getElementById("alerts-list");

        if (alerts.length === 0) {
            alertList.textContent = "No security alerts found.";
            return;
        }

        alertList.innerHTML = alerts.map(alert => `
            <div class="card">
                <h3>${alert.type}</h3>
                <p>IP: ${alert.ip_address}</p>
                <p>Failed Attempts: ${alert.failed_attempts}</p>
                <p>Severity: ${alert.severity}</p>
            </div>
        `).join("");

    } catch (error) {
        console.error("Alerts error:", error);
    }
}

// Upload and analyze log file
async function analyzeLogs() {
    const fileInput = document.getElementById("log-file");
    const file = fileInput.files[0];

    if (!file) {
        alert("Please select a .log file first.");
        return;
    }

    const formData = new FormData();
    formData.append("file", file);

    try {
        const response = await fetch(`${API_URL}/analyze`, {
            method: "POST",
            body: formData
        });

        const result = await response.json();

        if (!response.ok) {
            throw new Error(result.detail || "Analysis failed");
        }

        alert(`Analysis complete! Events: ${result.total_events}`);

        await loadEvents();
        await loadAlerts();

    } catch (error) {
        alert(error.message);
    }
}

// Load dashboard data when page opens
loadEvents();
loadAlerts();
