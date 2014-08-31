
months = [31,28,31,30,31,30,31,31,30,31,30,31]
leapmonths = [31,29,31,30,31,30,31,31,30,31,30,31]

sumMonths :: [Int] -> [Int]
sumMonths x = _sumMonths x 0

_sumMonths :: [Int] -> Int -> [Int]
_sumMonths (x:xs) acc = (x+acc):(_sumMonths xs (acc+x))
_sumMonths [] _ = []

sm =  init (1 : map (succ) (sumMonths months))
lm =  init (1 : map (succ) (sumMonths leapmonths))

isSun :: Int -> Int -> Bool
isSun day year
    | isLeap year =
        if day `elem` lm && (((day + start) `mod` 7) == 0) then True else False
    | otherwise = if day `elem` sm && (((day + start) `mod` 7) == 0) then True else False
    where start = startDay year

startDay :: Int -> Int
startDay year  
    | year == 1900 = 1
    | year > 1900 = (1 + sum [numDays y | y <- [1900..(year - 1)]]) `mod` 7

isLeap year = (year `mod` 4 == 0) && year /= 1900
numDays year 
    | isLeap year = 366
    | otherwise = 365

totalNum :: Int
totalNum = length $ filter (uncurry isSun) [(d,y) | d <- [1..366], y <- [1901..2000]]
    

main = do 
    putStrLn "HI"
    print (totalNum)
