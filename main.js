document.addEventListener('DOMContentLoaded', () => {
  fetch('/games')
    .then(response => response.json())
    .then(games => {
      const tbody = document.querySelector('#games-table tbody');
      games.forEach(g => {
        const row = document.createElement('tr');
        row.classList.add(g.color);
        row.innerHTML = `<td>${g.team}</td><td>${g.open}</td><td>${g.live}</td><td>${g.color}</td>`;
        tbody.appendChild(row);
      });
    });
});
