import Data.List (transpose)

calc :: [String] -> Int
calc ("+":xs) = sum (map read xs)
calc ("*":xs) = product (map read xs)
calc _ = 0

main :: IO ()
main = do
    input <- lines <$> getContents
    let processed = (transpose . map words . reverse) input
    print $ sum (map calc processed)