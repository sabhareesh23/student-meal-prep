let totalSpending = 0;
const visitedDays = {};

function loadDay(day) {
    fetch(`/api/meals/${day}`)
        .then(response => response.json())
        .then(data => {
            document.getElementById('meal-info').innerHTML = `
                <h2>📅 ${day.charAt(0).toUpperCase() + day.slice(1)}</h2>
                <h3>🍽️ Meals:</h3>
                <ul>${data.meals.map(m => `<li>${m}</li>`).join('')}</ul>
                <h3>🛒 Ingredients:</h3>
                <ul>${data.ingredients.map(i => `<li>${i}</li>`).join('')}</ul>
                <h3>💵 Daily Cost: $${data.daily_cost}</h3>
            `;

            if (!visitedDays[day]) {
                visitedDays[day] = data.daily_cost;
                totalSpending += data.daily_cost;
                document.getElementById('total').textContent = totalSpending.toFixed(2);
            }
        });
}