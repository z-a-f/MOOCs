function quiz()
    q1();
    q2();
    q3();
    q4();
    q5();
end

function q1()
    disp('----------------------');
    disp('Q1: Nothing to compute');
end

function q2()
    disp('----------------------');
    disp('Q2: Computing...');
    x = [1,2,2,3,...
        3,4,5,6,...
        6,6,8,10];
    y = -[890, 1411, 1560, 2220, ...
        2091, 2878, 3537, 3268,...
        3920, 4163, 5471, 5171];
    Theta = -[
        [1780.0, 530.9];...
        [569.6, 530.9];...
        [569.6, 530.9];...
        [1780.0, 530.9]
    ];
    J = zeros(size(Theta,1), 1);
    % h = zeros(size(x));
    for ii = 1:size(Theta,1)
        h = Theta(ii,1) + Theta(ii,2)*x;
        J(ii) = sum((h-y).^2); % Ignore constants
    end
    display('Minimum found at: ');
    disp(find(J==min(J))');
end

function q3()
    disp('----------------------');
    disp('Q3: Nothing to compute');
end

function q4()
    disp('----------------------');
    disp('Q4: Nothing to compute');
end

function q5()
    disp('----------------------');
    disp('Q5: Nothing to compute');
end

