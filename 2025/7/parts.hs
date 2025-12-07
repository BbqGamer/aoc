roll :: [a] -> [(a, a, a)]
roll (x:y:z:xs) = (x, y, z) : roll (y:z:xs)
roll _          = []

nState :: (Int, Int, Int) -> Int -> Int
nState (l, 0, r) val = val + l + r
nState _         _   = 0

sim :: ([Int], [Char]) -> ([Int], Int)
sim (state, row) = (zipWith nState windows state, count)
    where
        toSplit = map (\(v, c) -> if c == '^' then v else 0) (zip state row)
        windows = roll (0 : toSplit ++ [0])
        count = length (filter (> 0) toSplit)

simulate :: [String] -> [Int] -> Int -> ([Int], Int)
simulate [] state acc = (state, acc)
simulate (row : rows) state acc = 
    let (newState, cnt) = sim (state, row)
    in simulate rows newState (acc + cnt)

parseInput :: String -> [Int]
parseInput = map (\c -> if c == '.' then 0 else 1)

main = do
    input <- lines <$> getContents
    let (part2, part1) = simulate (tail input) (parseInput (head input)) 0
    print part1
    print (sum part2)