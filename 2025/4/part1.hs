import Data.List (transpose)

rolling :: Int -> [a] -> [[a]]
rolling k xs
    | length xs < k = []
    | otherwise     = take k xs : rolling k (tail xs)

rollingGrid w h grid = 
    let
        horizontal = map (rolling w) grid
        vertical = rolling h horizontal
        rolled = concatMap transpose vertical
    in
        map concat rolled

padGrid :: Int -> a -> [[a]] -> [[a]]
padGrid k padVal grid =
    let 
        paddingSize = k `div` 2
        padRow r = replicate paddingSize padVal ++ r ++ replicate paddingSize padVal
        horizontallyPadded = map padRow grid
        rowWidth  = length (head horizontallyPadded)
        emptyRow  = replicate rowWidth padVal
        verticalPad = replicate paddingSize emptyRow
    in 
        verticalPad ++ horizontallyPadded ++ verticalPad

count :: (a -> Bool) -> [a] -> Int
count p xs = length (filter p xs)

main :: IO ()
main = do
    input <- getContents
    let windows = rollingGrid 3 3 (padGrid 2 '.' (lines input))
    let counted = map (count (=='@')) (filter (\grid -> grid !! 4 == '@') windows)
    let removable = count (<=4) counted
    print removable
