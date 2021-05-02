function drawCircle() {
    let width = 12
    let height = 12
    let a = 5
    let b = 5
    let r = 5

    let mapping = Array(height).fill('.').map(() => Array(width).fill('.'))

    for (let y=0; y < height; y++) {
        for (let x=0; x < width; x++) {
            if (Math.abs((x-a) ** 2 + (y-b) ** 2) -  r ** 2 == 0)  {
                mapping[y][x] = '#'
            }
        }
    }
    console.log(mapping)     
    for (let line of mapping) {
        console.log(line.join())
    }       
}

drawCircle()