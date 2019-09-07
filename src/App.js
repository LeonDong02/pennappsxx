import React from 'react';
import './styles.scss';

function App() {
  return (
    <>
      <nav className="navbar is-spaced is-info">
        <div className="navbar-brand">
          <a href="/" className="navbar-item">
            <h1 className="subtitle has-text-primary is-3">Logo</h1>
          </a>
          <a id="navBurger" role="button" className="navbar-burger" data-target="navMenu" onClick={() => {
            document.getElementById("navBurger").classList.toggle('is-active');
            document.getElementById("navMenu").classList.toggle('is-active');
          }}>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
            <span aria-hidden="true"></span>
          </a>
        </div>
        <div id="navMenu" className="navbar-menu">
          <div className="navbar-start">
            <a className="navbar-item">
              About
            </a>
          </div>
          <div className="navbar-end">
            <div className="navbar-item">
              <div className="buttons are-large">
                <a href="" className="button is-rounded is-info">
                  Button 1
                </a>
                <a href="" className="button is-rounded is-primary">
                  Button 2
                </a>
              </div>
            </div>
          </div>
        </div>
      </nav>
      <section className="hero is-large is-info">
        <div className="hero-body">
          <div className="container">
            <h1 className="title">Words</h1>
            <h2 className="subtitle">Subtitle</h2>
          </div>
        </div>
      </section>
    </>
  );
}

export default App;
