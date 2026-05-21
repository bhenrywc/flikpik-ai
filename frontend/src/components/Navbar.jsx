function Navbar() {
  return (
    <nav className="navbar">
      <div className="brand">
        <span className="brand-mark">▶</span>
        <span>FlikPik</span>
      </div>
      <div className="nav-links">
        <a href="#discover">Discover</a>
        <a href="#ratings">Ratings</a>
        <a href="#trailers">Trailers</a>
      </div>
    </nav>
  );
}

export default Navbar;
