import Data.List (transpose)

rolling :: Int -> [a] -> [[a]]
rolling k xs
    | length xs < k = []
    | otherwise     = take k xs : rolling k (tail xs)


rollingGrid :: Int -> Int -> [[a]] -> [[[[a]]]]
rollingGrid w h grid = 
    let
        horizontal = map (rolling w) grid
        vertical = rolling h horizontal
        rolled = map transpose vertical
    in
        rolled

trans :: [[Char]] -> Char
trans window = 
    let 
        flat = concat window
    in 
        if flat !! 4 /= '@' then '.' else if (count (=='@') flat) <= 4 then '.' else '@'

    
transform :: [[Char]] -> [[Char]]
transform grid = map (map trans) (rollingGrid 3 3 (padGrid 2 '.' (grid)))

    
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

countRocks :: [[Char]] -> Int
countRocks grid = sum (map (count (=='@')) grid)

main :: IO ()
main = do
    start <- lines <$> getContents
    let transformed = transform start
    print ((countRocks start) - (countRocks transformed))