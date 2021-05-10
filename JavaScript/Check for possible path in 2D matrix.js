function checkPath(arr) {
    let q = [];
    q.push([0, 0])
    let directions = [[0, 1], [1, 0], [0, -1], [-1, 0]]
    while (q.length > 0) {
        let x = 0
        let y = 0
        let temp = q.shift()
        x, y = temp[0], temp[1]
        arr[x][y] = -1

        if (x === arr.length -1 && y === arr.length[0] - 1) {
            return true
        }
        for (let dir of directions) {
            let next_x = x + dir[0]
            let next_y = y + dir[1]
            if (next_x >=0 && next_x < arr.length-1 && next_y >= 0 && next_y < arr[0].length-1) {
                if (arr[next_x][next_y] != -1) {
                    q.push([next_x, next_y])
                }
            }
        }
    }
    console.log('arr')
    return false
    
}

var arr = [ [ 0, 0, 0, -1, 0 ],
            [ -1, 0, 0, -1, -1 ],
            [ 0, 0, 0, -1, 0 ],
            [ -1, 0, -1, 0, -1 ],
            [ 0, 0, -1, 0, 0 ] ]

checkPath(arr);