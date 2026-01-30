Friars&savages problem,also called wolves&sheep problem,is a classical planning problem.
There are 3 friars and 3 savages who are going to go across a river.The only boat can take 2 people(can't be more or less than 2)to go across the river.Each banks can't be in the condition of the number of savage(s) being more than friar(s),or else the friar(s) will be eaten by savage(s).
The version of wolves&sheep is similar,some versions even add vegetables,shepherd(s),or else what.
To solve the problem,we use pruning to form a state space tree but the tree is not complete because we use pruning to save the space,and then we use dfs to find a solution.
