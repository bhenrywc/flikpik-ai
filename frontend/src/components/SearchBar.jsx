import { useState } from "react";

function SearchBar({ onSearch, onReset }) {
  const [query, setQuery] = useState("");

  function handleSubmit(event) {
    event.preventDefault();

    if (!query.trim()) {
      onReset();
      return;
    }

    onSearch(query.trim());
  }

  return (
    <form className="search-panel" onSubmit={handleSubmit}>
      <input
        type="text"
        placeholder="Search Batman, Interstellar, Toy Story..."
        value={query}
        onChange={(event) => setQuery(event.target.value)}
      />
      <button type="submit">Search</button>
    </form>
  );
}

export default SearchBar;
