import Data.List (transpose)

calc :: [String] -> Int
calc ("+":xs) = sum (map read xs)
calc ("*":xs) = product (map read xs)
calc _ = 0

parseLine :: [Int] -> String -> [String]
parseLine [] _ = []
parseLine (l:lengths) str = take l str : parseLine lengths (drop (l + 1) str)

main :: IO ()
main = do
    input <- lines <$> getContents
    let part1 = sum . map calc . transpose . map words . reverse $ input
    print part1

    let values = init input
        ops = words (last input)
        columns = transpose (map words values)
        lengths = map (maximum . map length) columns
        parsed = map (parseLine lengths) values
        transposed = map transpose (transpose parsed)
    print $ sum (map (calc . uncurry (:)) (zip ops transposed))
