roll :: [a] -> [(a, a, a)]
roll (x:y:z:xs) = (x, y, z) : roll (y:z:xs)
roll _          = []

nState :: (Int, Int, Int) -> Int -> Int
nState (l, 0, r) val = val + l + r
nState _         _   = 0

sim :: ([Int], [Char]) -> [Int]
sim (state, row) = zipWith nState windows state
    where
        toSplit = map (\(v, c) -> if c == '^' then v else 0) (zip state row)
        windows = roll (0 : toSplit ++ [0])

simulate [] state = state
simulate (row : rows) state = simulate rows (sim (state, row))

parseInput :: String -> [Int]
parseInput = map (\c -> if c == '.' then 0 else 1)

main = do
    input <- lines <$> getContents
    let simulated = simulate (tail input) (parseInput (head input))
    print (sum simulated)