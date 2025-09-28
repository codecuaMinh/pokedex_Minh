const container = document.getElementById("pokemon-container");

async function getPokemon(id) {
  const url = `https://pokeapi.co/api/v2/pokemon/${id}`;
  const res = await fetch(url);
  const data = await res.json();
  return data;
}

async function displayPokemons() {
  for (let i = 1; i <= 20; i++) {
    // 👉 sửa lại từ 20 → 60
    const pokemon = await getPokemon(i);

    const card = document.createElement("div");
    card.classList.add("pokemon-card");

    // Thẻ chứa thông tin Pokémon, gồm phần ẩn chi tiết
    card.innerHTML = `
  <h3>#${pokemon.id} ${pokemon.name}</h3>
  <img src="${pokemon.sprites.front_default}" alt="${pokemon.name}" />
  <div class="types">
    ${pokemon.types
      .map(
        (t) => `
      <img class="type-icon" src="https://raw.githubusercontent.com/duiker101/pokemon-type-svg-icons/master/icons/${t.type.name}.svg" alt="${t.type.name}" title="${t.type.name}" />
    `
      )
      .join("")}
  </div>
  <div class="extra-info">
    <p><strong>Height:</strong> ${pokemon.height}</p>
    <p><strong>Weight:</strong> ${pokemon.weight}</p>
  </div>
`;

    // Rê chuột vào thì hiện info

    container.appendChild(card);
  }
}

// Gọi hàm để chạy
displayPokemons();
