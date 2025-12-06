import Data.List (transpose)
import Data.Char (digitToInt)

calc :: [String] -> Int
calc ("+":xs) = sum (map read xs)
calc ("*":xs) = product (map read xs)
calc _ = 0

noSpace s = filter (/=' ') s

-- convertCol col = map digitToInt col

calc2 ("+", xs) = sum (map read xs)
calc2 ("*", xs) = product (map read xs)

parseLine [] str = []
parseLine (l : lengths) str =
    take l str : parseLine lengths (drop (l + 1) str)


main :: IO ()
main = do
    input <- lines <$> getContents
    let processed = (transpose . map words . reverse) input 
    print $ sum (map calc processed)

    let numbers = init input
    let ops = words (last input)
    let processed = (transpose . map words) numbers

    let lengths = map (maximum . map length) processed
    let parsed = map (parseLine lengths) numbers
    let transposed = map transpose (transpose parsed)
    let zipped = zip ops transposed
    print zipped
    print (sum (map calc2 zipped))
