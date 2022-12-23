%%Random Walk

%%
%Consider an island defined by a one-dimensional grid of length 100 units and the initial position of the 
% squirrel is 40 units from the left (tagged 0), create a simulation of the squirrel hooping on the island over time.

start_pos= input("Starting Position?")
grid_length= input("Grid length?")
curr_pos = start_pos;
num_hops = 1;
while (curr_pos > 0 && curr_pos < grid_length)
        toss = rand(1);
    if (toss < 0.5)
        curr_pos = curr_pos - 1;
    elseif (toss >= 0.5)
        curr_pos = curr_pos + 1;
    end
    stem(curr_pos,0);
    xlim([0,grid_length]);
    F=getframe;
    movie(F);
    num_hops= num_hops+1


end

%%
%Does the squirrel eventually fall of and die or does she just bounce on and off on the island in a never ending fashion? 
% Play your simulation and justify your answer.

start_pos= 5
grid_length= 10
curr_pos = start_pos;
num_hops = 1;
while (curr_pos > 0 && curr_pos < grid_length)
        toss = rand(1);
    if (toss < 0.5)
        curr_pos = curr_pos - 1;
    elseif (toss >= 0.5)
        curr_pos = curr_pos + 1;
    end
    num_hops= num_hops+1
end
