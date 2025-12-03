parse :: String -> Int
parse ('L':xs) = - (read xs :: Int)
parse ('R':xs) =   read xs :: Int

hits :: Int -> Int -> (Int, Int)
hits s m
    | m >= 0  = (mod (s + m) 100, div (s + m) 100)
    | m < 0  = (mod (s + m) 100, div ((if s == 0 then 0 else 100 - s) - m) 100)

applyMoves :: [Int] -> (Int, Int)
applyMoves = foldl step (50, 0)
    where
        step :: (Int, Int) -> Int -> (Int, Int)
        step (state, total) move =
            let (newState, val) = hits state move
                newTotal = total + val
            in (newState, newTotal)

main :: IO ()
main = do
    contents <- getContents
    let (finalState, totalSum) = applyMoves (map parse (lines contents))
    print totalSum
