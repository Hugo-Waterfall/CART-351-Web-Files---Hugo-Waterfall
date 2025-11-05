//STEP 2.3
window.onload = runScript

let colourSelected = false
let val = 0;

function runScript(){

    //create a block the player can move mouse over and listen for event
    let player = document.querySelector("#player")
    player.addEventListener("mousemove", callback_hoversquare)
    player.setAttribute("timeHovered",0)

    function callback_hoversquare(event){

        //if the colour hasnt been selected yet
        //increments the hue of the square as the user hovers over square
        if(!colourSelected){
            val = parseInt(this.getAttribute("timeHovered"))
            val = (val + 1) % 360
            this.setAttribute("timeHovered", val)
            player.style.background =  "hwb("+val+" 0% 0%)"

        }
    }

    //callback for select colour function
    //triggers when user clicks the square
    player.addEventListener("click", callback_select)

    function callback_select(event){ 
        //trigger boolean that locks colours and then starts listeneing to key presses
        colourSelected = true

        //holds the colour string corresponding the colour that the user picked on the square
        const hwbValue = "hwb("+val+" 0% 0%)";

            //fills spans in the html file with corresponding information. Also colors the data in with the actual color
            document.getElementById("colorOutput").innerText = hwbValue;
            document.getElementById("colorOutput").style.color = hwbValue;

            //calls the fetch request function when the user clicks the color on the square
            sendColorToServer(hwbValue);

    }

    window.addEventListener("keydown", keyClickCallback)

    function keyClickCallback(event){

        if(colourSelected){

            }
        }
    }

function displayInfo(infoText, x, y) {
    push();
    fill("#ffffff");
    textAlign(CENTER);
    text(infoText.toUpperCase(), x, y);
    pop();
}

//STEP 2.4
//the function which holds the fetch request, which not only sends the json object of the colour to the server, but also returns whether that colour is already in the server txt file
function sendColorToServer(hwbColor) {

    fetch("/postDataFetch", {method: "POST", headers: { "Content-Type": "application/json"}, body: JSON.stringify({color:hwbColor})})

    .then(response => response.json())
    .then(data => { console.log("server replied: ", data);

        const statusMessage = document.getElementById("statusMessage");

        statusMessage.innerText = data.message

    })

    .catch(error => console.error("Error: ", error));

}
