life_expectancy=0;
    for l=1:30
    grid_length=15;
    start_pos=1; %vary for different starting positions
    [num_hops] = Lab2_LifeExpectancy(grid_length, start_pos);
    life_expectancy = life_expectancy+num_hops;
    end
    avg=life_expectancy/30
