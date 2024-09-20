import './styles/style.css'
import './styles/globals.css'
import './styles/grid.css'

document.querySelector('#itemsSection').innerHTML = `
    <div class="itemsSection">
        <div class="container">
            <div class="col6 itemsBox">
                <img src="/person-iPhone.JPG" width="100%" heigth="100%" />
                <div class="itemsBoxContent">
                    <h2>iPhone</h2>
                    <p class="whiteP">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when.</p>
                    <button>
                        SEE MORE >
                    </button>
                </div>
            </div>
            <div class="col6 itemsBox">
                <img src="/samsung.JPG" width="100%" heigth="100%" />
                <div class="itemsBoxContent">
                    <h2>Samsung</h2>
                    <p class="whiteP">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when.</p>
                    <button>
                        SEE MORE >
                    </button>
                </div>
            </div>
            <div class="col6 itemsBox">
                <img src="/huawei.JPG" width="100%" heigth="100%" />
                <div class="itemsBoxContent">
                    <h2>Huawei</h2>
                    <p class="whiteP">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when.</p>
                    <button>
                        SEE MORE >
                    </button>
                </div>
            </div>
            <div class="col6 itemsBox">
                <img src="/oppo.JPG" width="100%" heigth="100%" />
                <div class="itemsBoxContent">
                    <h2>Oppo</h2>
                    <p class="whiteP">Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when.</p>
                    <button>
                        SEE MORE >
                    </button>
                </div>
            </div>
        </div>
    </div>
`
