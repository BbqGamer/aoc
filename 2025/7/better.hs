mapper (val, '^') = val
mapper (val, _) = 0

roll :: [a] -> [(a, a, a)]
roll xs
    | length xs < 3 = []
    | otherwise     = (xs !! 0, xs !! 1, xs !! 2) : roll (tail xs)

nState (l, 0, r) val = val + r + l
nState (l, m, r) val = 0

sim :: ([Int], [Char]) -> [Int]
sim (state, row) = 
    let
        toSplit = map mapper (zip state row)
        windows = roll ([0] ++ toSplit ++ [0])
        newState = zipWith nState windows state
    in 
        newState

simulate [] state = state
simulate (row : rows) state = simulate rows (sim (state, row))

main = do
    input <- lines <$> getContents
    let state = map (\x -> if x == '.' then 0 else 1) (head input)
    let simulated = simulate (tail input) state
    print simulated
    print (sum simulated)