import Data.List (sort, sortOn, tails, group)
import Data.List.Split (splitOn)
import qualified Data.Map as Map
import qualified Data.Set as Set
import System.Environment (getArgs)

data Point3D = Point3D !Int !Int !Int
    deriving (Show, Eq, Ord)

type Edge = (Point3D, Point3D)
type PointMap = (Map.Map Point3D Int)
type GroupMap = (Map.Map Int (Set.Set Point3D))

processLine :: String -> Point3D
processLine line = 
    case map read (splitOn "," line) of
        [x, y, z] -> Point3D x y z
        _         -> error $ "Invalid line: " ++ line

dist :: Point3D -> Point3D -> Float
dist (Point3D x1 y1 z1) (Point3D x2 y2 z2) =
    sqrt $ fromIntegral $ (x2 - x1)^2 + (y2 - y1)^2 + (z2 - z1)^2

updateGraph :: PointMap -> GroupMap -> Edge -> (PointMap, GroupMap)
updateGraph pointMap groupMap (a, b) =
    let 
        idA = Map.findWithDefault 0 a pointMap
        idB = Map.findWithDefault 0 b pointMap
    in
        if idA == idB 
        then (pointMap, groupMap)
        else 
            let mergedGroups = Map.adjust (Set.union (Map.findWithDefault Set.empty idB groupMap)) idA groupMap
            in (Map.map (\v -> if v == idB then idA else v) pointMap, Map.delete idB mergedGroups)


part2 pointMap groupMap [] = return (-1)
part2 pointMap groupMap (edge@(Point3D x1 _ _, Point3D x2 _ _) : edges) = do
    let (newMap, newGroup) = updateGraph pointMap groupMap edge
    if Map.size newGroup == 1
       then return (x1 * x2)
       else part2 newMap newGroup edges

main :: IO ()
main = do
    args <- getArgs
    input <- getContents
    
    let n = read (head args) :: Int
        points = map processLine (lines input)
        edges = [ ((p1, p2), dist p1 p2) | (p1:rest) <- tails points, p2 <- rest ]
        sortedEdges = sortOn snd edges
        edgesToProcess = map fst sortedEdges

        initialMap = Map.fromList (zip points [1..])
        initialGroups = Map.fromList (zip [1..] ([Set.singleton x | x <- points]))
    
    res <- part2 initialMap initialGroups edgesToProcess

    print res