let totalSpending = 0;
const visitedDays = {};

function loadDay(day, btn) {
    // Remove active class from all buttons
    document.querySelectorAll('.days button').forEach(b => b.classList.remove('active'));
    btn.classList.add('active');

    fetch(`/api/meals/${day}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('meal-info').innerHTML = `
                <h2>📅 ${day.charAt(0).toUpperCase() + day.slice(1)}</h2>
                <h3 style="margin:15px 0 10px">🍽️ Meals</h3>
                <ul>${data.meals.map(m => `<li>🥘 ${m}</li>`).join('')}</ul>
                <h3 style="margin:15px 0 10px">🛒 Ingredients</h3>
                <ul>${data.ingredients.map(i => `<li>• ${i}</li>`).join('')}</ul>
                <h3 style="margin:15px 0 10px">💵 Daily Cost: $${data.daily_cost}</h3>
            `;

            if (!visitedDays[day]) {
                visitedDays[day] = data.daily_cost;
                totalSpending += data.daily_cost;
                document.getElementById('total').textContent = totalSpending.toFixed(2);
            }
        });
}
function suggestMeal() {
    const preference = document.getElementById('preference').value;
    if (!preference) return;

    const suggestionDiv = document.getElementById('suggestion');
    suggestionDiv.style.display = 'block';
    suggestionDiv.textContent = 'Thinking...';

    fetch('/api/suggest', {
        method: 'POST',
        headers: {'Content-Type': 'application/json'},
        body: JSON.stringify({preference: preference})
    })
    .then(response => response.json())
    .then(data => {
        suggestionDiv.textContent = data.suggestion;
    })
    .catch(() => {
        suggestionDiv.textContent = 'Something went wrong. Try again!';
    });
}
