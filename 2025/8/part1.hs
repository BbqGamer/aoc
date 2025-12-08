import Data.List (sort, sortOn, tails, group)
import Data.List.Split (splitOn)
import qualified Data.Map as Map
import System.Environment (getArgs)

data Point3D = Point3D !Int !Int !Int
    deriving (Show, Eq, Ord)

type Edge = (Point3D, Point3D)

processLine :: String -> Point3D
processLine line = 
    case map read (splitOn "," line) of
        [x, y, z] -> Point3D x y z
        _         -> error $ "Invalid line: " ++ line

dist :: Point3D -> Point3D -> Float
dist (Point3D x1 y1 z1) (Point3D x2 y2 z2) =
    sqrt $ fromIntegral $ (x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2

updateGraph :: Int -> Map.Map Point3D Int -> Edge -> Map.Map Point3D Int
updateGraph newId pointMap (a, b) =
    case (Map.lookup a pointMap, Map.lookup b pointMap) of
        (Nothing, Nothing) -> 
            Map.insert a newId $ Map.insert b newId pointMap
        (Just idA, Nothing) -> 
            Map.insert b idA pointMap
        (Nothing, Just idB) -> 
            Map.insert a idB pointMap
        (Just idA, Just idB) -> 
            if idA == idB 
            then pointMap 
            else Map.map (\v -> if v == idB then idA else v) pointMap

main :: IO ()
main = do
    args <- getArgs
    input <- getContents
    
    let n = read (head args) :: Int
        points = map processLine (lines input)
        edges = [ ((p1, p2), dist p1 p2) | (p1:rest) <- tails points, p2 <- rest ]
        sortedEdges = sortOn snd edges
        edgesToProcess = map fst $ take n sortedEdges
        finalMap = foldl (\acc (id, edge) -> updateGraph id acc edge) Map.empty (zip [n, n-1 ..] edgesToProcess)
        componentSizes = map length $ group $ sort $ Map.elems finalMap
        top3Product = product $ take 3 $ reverse $ sort componentSizes

    print top3Product