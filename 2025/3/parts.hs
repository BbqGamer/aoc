argmax :: (Ord a) => [a] -> Int
argmax xs = fst $ foldl1 keepFirstMax (zip [0..] xs)
  where
    keepFirstMax acc x
      | snd x > snd acc = x
      | otherwise       = acc

biggest 0 line = ""
biggest n line =
    let amax = argmax (take (length line - (n - 1)) line)
    in (line !! amax) : biggest (n - 1) (drop (amax + 1) line)

solve n contents = sum (map (read . biggest n) (lines contents))

main = do
    contents <- getContents
    print (solve 2 contents)
    print (solve 12 contents)