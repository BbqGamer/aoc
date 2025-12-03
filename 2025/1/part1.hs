parse :: String -> Int
parse ('L':xs) = - (read xs :: Int)
parse ('R':xs) =   read xs :: Int

applyMoves :: [Int] -> (Int, Int)
applyMoves = foldl step (50, 0)
    where
        step :: (Int, Int) -> Int -> (Int, Int)
        step (state, total) move =
            let newState = mod (state + move) 100
                newTotal = total + (if state == 0 then 1 else 0)
            in (newState, newTotal)

main :: IO ()
main = do
    contents <- getContents
    let (finalState, totalSum) = applyMoves (map parse (lines contents))
    print totalSum
