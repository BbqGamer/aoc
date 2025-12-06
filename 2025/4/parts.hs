import Data.List (transpose)

rolling :: Int -> [a] -> [[a]]
rolling k xs
    | length xs < k = []
    | otherwise     = take k xs : rolling k (tail xs)

rollingGrid :: Int -> Int -> [[a]] -> [[[[a]]]]
rollingGrid w h = map transpose . rolling h . map (rolling w)

trans :: [[Char]] -> Char
trans window
    | center /= '@'     = '.'
    | rockCount <= 4    = '.'
    | otherwise         = '@'
  where
    flat = concat window
    center = flat !! 4
    rockCount = length (filter (== '@') flat)

transform :: [[Char]] -> [[Char]]
transform = map (map trans) . rollingGrid 3 3 . padGrid 1 '.'

padGrid :: Int -> a -> [[a]] -> [[a]]
padGrid padding padVal grid = verticalPad ++ map padRow grid ++ verticalPad
  where
    padRow = (replicate padding padVal ++) . (++ replicate padding padVal)
    rowWidth = length (head grid) + 2 * padding
    verticalPad = replicate padding (replicate rowWidth padVal)

countRocks :: [[Char]] -> Int
countRocks = length . filter (== '@') . concat

repeatUntilStable :: [[Char]] -> [[Char]]
repeatUntilStable grid
    | grid == new = grid
    | otherwise   = repeatUntilStable new
  where
    new = transform grid

main :: IO ()
main = do
    start <- lines <$> getContents
    let part1 = transform start
        part2 = repeatUntilStable part1
        startCount = countRocks start
    print (startCount - countRocks part1)
    print (startCount - countRocks part2)