import './styles/style.css'
import './styles/globals.css'
import './styles/grid.css'

document.querySelector('#navBar').innerHTML = `
    <div class="navbar">
        <div class="container">
            <div class="col1 logo">
                <img src="./../public/logoWhite.png" width="3840" height="2160" />
            </div>
            <div class="col11 menuOptions">
                <div class="menuOpt">
                    <h4>SIGN OUT</h4>
                    <hr />
                </div>
                <div class="menuOpt">
                    <h4>SIGN IN</h4>
                    <hr />
                </div>
                <div class="menuOpt">
                    <h4>PRODUCTS</h4>
                    <hr />
                </div>
                <div class="menuOpt navOptActive">
                    <h4>HOME</h4>
                    <hr />
                </div>
            </div>
        </div>
    </div>
`
