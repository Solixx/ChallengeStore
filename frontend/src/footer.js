import "./styles/style.css";
import "./styles/globals.css";
import "./styles/grid.css";

document.querySelector("#footer").innerHTML = `
    <footer class="container">
        <div class="col12 footerLine" > 
            <hr />
        </div>
        <div class="col12 footerTop">
            <div class="logo">
                <img src="./../public/logoWhite.png" width="3840" height="2160" />
            </div>
            <div class="footerFrase">
                <h1 class="title">U</h1>
                <h1 class="title">P</h1>
                <h1 class="title">G</h1>
                <h1 class="title">R</h1>
                <h1 class="title">A</h1>
                <h1 class="title">D</h1>
                <h1 class="title">E</h1>
            </div>
        </div>
        <div class="col2 footerMidLeft">
            <p>Navigation</p>
            <div class="footerOptionsList"> 
                <div class="footerOption">
                    <hr />
                    <a href="./index.html"><h5>HOME</h5></a>
                </div>
                <div class="footerOption">
                    <hr />
                    <a href="./about.html"><h5>PRODUCTS</h5></a>
                </div>
                <div class="footerOption">
                    <hr />
                    <a href="./services.html"><h5>SIGN IN</h5></a>
                </div>
                <div class="footerOption">
                    <hr />
                    <a href="./contact.html"><h5>SIGN OUT</h5></a>
                </div>
            </div>
        </div>
        <div class="col2 footerMidLeft">
            <p>Categories</p>
            <div class="footerOptionsList"> 
                <div class="footerOption">
                    <hr />
                    <a href="./index.html"><h5>PHONES</h5></a>
                </div>
                <div class="footerOption">
                    <hr />
                    <a href="./about.html"><h5>WATCHES</h5></a>
                </div>
                <div class="footerOption">
                    <hr />
                    <a href="./services.html"><h5>TABLETS</h5></a>
                </div>
                <div class="footerOption">
                    <hr />
                    <a href="./contact.html"><h5>PCS</h5></a>
                </div>
            </div>
        </div>
        <div class="col8 footerMidRight">
            <div class="footerRightInfos">
                <hr />
                <div class="footerRightInfosText">
                    <p>Phone</p>
                    <h4>123-456-789</h4>
                </div>
            </div>
            <div class="footerRightInfos">
                <hr />
                <div class="footerRightInfosText">
                    <p>Email</p>
                    <h4>exemple@gmail.com</h4>
                </div>
            </div>
            <div class="footerRightInfos">
                <hr />
                <div class="footerRightInfosText">
                    <p>Socials</p>
                    <div class="socials">
                        <svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 50 50" width="30px" height="30px"><path d="M 6.9199219 6 L 21.136719 26.726562 L 6.2285156 44 L 9.40625 44 L 22.544922 28.777344 L 32.986328 44 L 43 44 L 28.123047 22.3125 L 42.203125 6 L 39.027344 6 L 26.716797 20.261719 L 16.933594 6 L 6.9199219 6 z"/></svg>                   
                        <svg xmlns="http://www.w3.org/2000/svg"  viewBox="0 0 50 50" width="30px" height="30px"><path d="M 16 3 C 8.8324839 3 3 8.8324839 3 16 L 3 34 C 3 41.167516 8.8324839 47 16 47 L 34 47 C 41.167516 47 47 41.167516 47 34 L 47 16 C 47 8.8324839 41.167516 3 34 3 L 16 3 z M 16 5 L 34 5 C 40.086484 5 45 9.9135161 45 16 L 45 34 C 45 40.086484 40.086484 45 34 45 L 16 45 C 9.9135161 45 5 40.086484 5 34 L 5 16 C 5 9.9135161 9.9135161 5 16 5 z M 37 11 A 2 2 0 0 0 35 13 A 2 2 0 0 0 37 15 A 2 2 0 0 0 39 13 A 2 2 0 0 0 37 11 z M 25 14 C 18.936712 14 14 18.936712 14 25 C 14 31.063288 18.936712 36 25 36 C 31.063288 36 36 31.063288 36 25 C 36 18.936712 31.063288 14 25 14 z M 25 16 C 29.982407 16 34 20.017593 34 25 C 34 29.982407 29.982407 34 25 34 C 20.017593 34 16 29.982407 16 25 C 16 20.017593 20.017593 16 25 16 z"/></svg>
                        <svg width="30px" height="30px" viewBox="0 0 24 24" xmlns="http://www.w3.org/2000/svg" xml:space="preserve"><path d="M19.589 6.686a4.793 4.793 0 0 1-3.77-4.245V2h-3.445v13.672a2.896 2.896 0 0 1-5.201 1.743l-.002-.001.002.001a2.895 2.895 0 0 1 3.183-4.51v-3.5a6.329 6.329 0 0 0-5.394 10.692 6.33 6.33 0 0 0 10.857-4.424V8.687a8.182 8.182 0 0 0 4.773 1.526V6.79a4.831 4.831 0 0 1-1.003-.104z"/></svg>
                    </div>
                </div>
            </div>
        </div>
    </footer>
`;
