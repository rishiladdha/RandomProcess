function [num_hops] = RandomWalk3(grid_length, start_pos)
    curr_pos=start_pos;
    num_hops=1;
    while (curr_pos >0 && curr_pos<grid_length)
      toss=rand(1);
      if (toss < 0.5)
        curr_pos = curr_pos- 1;
      elseif (toss >= 0.5)
        curr_pos = curr_pos + 1;
      end
     
      num_hops=num_hops+1;
    end
    num_hops
