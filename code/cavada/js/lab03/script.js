let board = ['-','-','-','-','-','-','-','-','-']

const divBoard = document.querySelector('#board')
let legend = document.querySelector('legend')
let checkSpaces

//make board
i = 1
while (i < 10) {

    let space = document.createElement('div') 
    space.classList= 'space'
    iStr = 'spc'+String(i)
    space.id = iStr
    divBoard.appendChild(space)
    let spaceBtn = document.createElement('button')
    spaceBtn.classList.add= ('space-btn')
    spaceBtn.style.display=('block')
    spaceBtn.style.width=('100%')
    iStr = 'btn'+String(i)
    spaceBtn.id = iStr
    space.appendChild(spaceBtn)
    i++
}
const Spaces = {
    1:document.querySelector('#spc1'),
    2:document.querySelector('#spc2'),
    3:document.querySelector('#spc3'),
    4:document.querySelector('#spc4'),
    5:document.querySelector('#spc5'),
    6:document.querySelector('#spc6'),
    7:document.querySelector('#spc7'),
    8:document.querySelector('#spc8'),
    9:document.querySelector('#spc9')
}

const boardSpaces = {
    1:document.querySelector('#btn1'),
    2:document.querySelector('#btn2'),
    3:document.querySelector('#btn3'),
    4:document.querySelector('#btn4'),
    5:document.querySelector('#btn5'),
    6:document.querySelector('#btn6'),
    7:document.querySelector('#btn7'),
    8:document.querySelector('#btn8'),
    9:document.querySelector('#btn9')
}

function check(board) {
    let test = board.slice()

    checkSpaces = {
    'h1' : test.slice(0,3),
    'h2' : test.slice(3,6),
    'h3' : test.slice(6,9),
    'v1' : [test.slice(0,1).toString(),test.slice(3,4).toString(),test.slice(6,7).toString()],
    'v2' : [test.slice(1,2).toString(),test.slice(4,5).toString(),test.slice(7,8).toString()],
    'v3' : [test.slice(2,3).toString(),test.slice(5,6).toString(),test.slice(8,9).toString()],
    'd1' : [test.slice(0,1).toString(),test.slice(4,5).toString(),test.slice(8,9).toString()],
    'd2' : [test.slice(2,3).toString(),test.slice(4,5).toString(),test.slice(6,7).toString()]
    }
    for (key in checkSpaces) {
        
        console.log(key,':',checkSpaces[key])
        if (checkSpaces[key] === ['X','X','X']) {
            winner = 'X'
            
        } else if (checkSpaces[key] === ['O','O','O']) {
            winner = 'O'
        }
    
    }
    alert(winner)
    return winner
}

let token
let counter = 1
let tokens = ['O','X']
let winner
for (key in boardSpaces) {
    let index = key
    let boardSpace = boardSpaces[key]
    let spc = Spaces[key]
    
    boardSpace.addEventListener('click',function() {
        boardSpace.style.display = 'none'
        if (counter % 2 === 0) {
            legend.innerText = 'Player X'
            token = tokens[0]
            spc.innerText = token
            spc.style.fontSize = ('20vh')
            console.log(token)
            console.log(spc)
            let key = Object.keys(Spaces).find(k=>Spaces[k]===spc)
            console.log(key)
            board.splice(key-1,1,token)
            console.log(board)
            winner = check(board)
            console.log(winner)
            if (winner == 'X' || winner == 'O') {
                alert(winner) 
            }

        } else {
            legend.innerText = 'Player O'
            token = tokens[1]
            boardSpace.innerText = token
            spc.style.fontSize = ('20vh')
            spc.innerText = token
            console.log(token)
            console.log(spc)
            let key = Object.keys(Spaces).find(k=>Spaces[k]===spc)
            console.log(key)
            board.splice(key-1,1,token)
            console.log(board)
            winner = check(board)   
            console.log(winner)     
            if (winner != undefined) {
                alert(winner) 
            }         
        }
    counter++
    })
}

    
 
