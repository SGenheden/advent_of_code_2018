require('../modules/AugmentString')()

app(`.|#..|#.|.#.#..|.#..##......#...#..#...|.#.#|.|..#
.|||.##.#|#..|#.|#.|.............|.....|.....|#||.
|...#.||.#.|.|#.#....##..||#...#|..|#...##...|#...
...|.##|...|.||...##.#.##.|...#.|#..|..........#.#
#..#....#.#.|....#...#|#....|.###........|#.....#.
#.##.#..#|##.|||.|..|.|#.....|#.....|||||.#.#.|#..
..|....#|...#...#|##...#...|.|...#.#.||.|.|..#.|#.
..##.|..||...|.#..#.|.#..|..#.###.#....###........
#.....#|.....#.|#....#.|.||||.##..||.#.|.#|.....#|
....##...#.......#..|..#||...#||#.|.|.||..#.|||##.
###.##..||..###.#..#.#.|.....#.|#..#.#|...|#..|.#.
...#|###|||.||...#.||..##..|#|...||#....#...||.#..
|..####..#.....|..#..||.#.....##|....||..|......#|
|##...|.#......#||#|......#|#.|#....|..#||....|.||
...#..||#.||..#|.###|.#.|...|...|##|...##....|.||#
.||.|####.#|..|#.....|..#.#.|#.....|.|...##..|....
|.#.........#|....|....#||........#.#.....#....|||
...|#|..#|...|.|..#.##|#..|......#.....|.||..#||#|
.#.....||.#..##.|....#...|.|.#...|.#...|#|..|#|#..
.#.#|.|#.#.|.#.#.||.....|#..|.##|#.##..#|..|#|.|..
....#......|.....##.......##....|#.........#.....|
.......|.......#|...#.|#|.#||...#|..|..||.#...|...
#|..#|....|..||.||..|..##|#..##..#|.#.#.#|.|...|#.
..#.|#.#..|#..#.|.....#|.#..#...#|....|.|.....|...
.#.##|......#.......|#||.|.....#..#.#...|##.#....|
...##..#..#.||..|.|#..#.#.....#......|.|..|.....|.
.|##..|.|..#||....|....|..#.....|..#...#...#|#||#.
...#|#.....#..|.|.|...|##...||###....||...#......#
.#|..#..........|.#......|...#..|#|..#.|#|......|.
#..#.......||#|..##.#.|...#.|.|||#.....#..|......#
....|..|#..#..#.......#..|...#.#.|#.#.#.##||....|.
#|#|#.|..|..|.#...|..#.|||......#.........|#.|..||
|..||.|..|....#.|..#...#..#.|..##...#||..|........
.##..#||..|||.##|###|...###...|...##|......|.|.#..
#..##..#....|..|..||.#|.|.#.|.....|.||..|#.|||.##.
....#|...|...|.|#....##.#.|.#......##..|.|..#.|#..
#||..||#..###||....|..|.|...#..#...|.#..###..|#.|.
.#||.|#..##|#|......|.....#|#|......#..||##|.##..|
.#|.|..|..###|.#|....||...|...||.||...|...##..||..
||#........#..##.....|.|#......|...#..|.##..#...|.
.#.#|........||...|#.||.#|.|...|#.#..|....|.|..#..
.|.|||||....|.#|...###..|...||.||..........#|...##
#||..#...#.#.##|#.|..##..#|#....#.|.|#|....#|.|##|
|..|........|.#..........#|..##....|.#|.#.#.|#...|
.#.##|..##.#..#...|..#||#.|.#...#|...|#.#..|#..|.|
.|.|.#..|#...#.|....#.#......#..|.....|#..........
|.#...|#...|........#....#.|.#.#....#....|..|..##.
.|....#.#........|..|..|##....###..#..#..#..|#....
.|#..#....##...#.....#|##....|##........|.#.#|..|.
|.|#.|.#||#....||.#|...#...#.|##......#.|...|..#|#`)

function app (input) {  
    let map = {}
    let upperBounds = { c: input.lines()[0].length, r: input.lines().length }

    input.lines().forEach((line, r) => {
        line.split('').forEach((char, c) => {
            map[`${c},${r}`] = { c, r, char }
        })
    })

    function get (map, c, r) {
        let val = map[`${c},${r}`]

        if (c < 0 || c > upperBounds.c || r < 0 || r > upperBounds.r || !val) {
            return {}   
        }

        return val
    }

    for (let i = 0; i < 10; ++i) {
        let cpMap = JSON.parse(JSON.stringify(map))

        for (let [key, value] of Object.entries(map)) {
            let [c, r] = key.split(',').map(Number)

            let adj = [
                get(cpMap, c - 1, r - 1), get(cpMap, c, r - 1), get(cpMap, c + 1, r - 1),
                get(cpMap, c - 1, r), get(cpMap, c + 1, r),
                get(cpMap, c - 1, r + 1), get(cpMap, c, r + 1), get(cpMap, c + 1, r + 1),
            ]

            let numWoods = adj.filter(el => el.char === '|').length
            let numLumber = adj.filter(el => el.char === '#').length

            if (numWoods >= 3 && get(cpMap, c, r).char === '.') {
                map[`${c},${r}`].char = '|' 
            }
            
            if (numLumber >= 3 && get(cpMap, c, r).char === '|') {
                map[`${c},${r}`].char = '#' 
            }

            if (get(cpMap, c, r).char === '#') {
                map[`${c},${r}`].char = (numLumber >= 1 && numWoods >= 1) ? '#' : '.'
            }
        }
    }

    let woddens = Object.values(map).filter(square => square.char === '|').length
    let lumbers = Object.values(map).filter(square => square.char === '#').length
    console.log(woddens * lumbers)
    return woddens * lumbers
}