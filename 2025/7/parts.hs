import qualified Data.Map as Map
import qualified Data.Set as Set

merge (i, xs) =
    map (\(a, b) -> ((i, a), b)) xs

move elem = (\(a, b) -> (succ a, b))

simulate splitters beams limN limM 
    | Set.null beams = 0
    | otherwise =
        let 
            moved = Set.map (\(a, b) -> (succ a, b)) beams
            filtered = Set.filter (\(a, b) -> a >= 0 && b >= 0 && a <= limN && b <= limM) moved
            toSplit = filtered `Set.intersection` splitters
            noSplit = filtered `Set.difference` toSplit
            splitted = Set.unions (Set.map (\(a, b) -> Set.fromList ([(a, b - 1), (a, b + 1)])) toSplit)
            newbeams = splitted `Set.union` noSplit
        in
            simulate splitters newbeams limN limM + Set.size toSplit

main = do
    input <- lines <$> getContents

    let zipped = zip [0..] (map (zip [0..]) input)
    let dict = Map.fromList (concat (map merge zipped))

    let start = Map.keysSet (Map.filter (== 'S') dict)
    let splitters = Map.keysSet (Map.filter (== '^') dict)

    let (n, m) = maximum (Set.toList splitters)
    let simulated = simulate splitters start n m
    print simulated