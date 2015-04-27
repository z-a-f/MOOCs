function LinearRegressionCost
    a = -5;
    b = -5;
    x = -1:0.01:1;
    Theta0 = -20:10;
    Theta1 = -20:10;
    y = linearEquation(a,b,x,[length(Theta0), length(Theta1)]);
    h = linearHypothesis(Theta0, Theta1, x);
    J = linearCost(y, h, length(x));
    mesh(Theta0, Theta1,J);
    xlabel('\Theta_0'); ylabel('\Theta_1'); zlabel('J(\Theta_0,\Theta_1)');
end

function J = linearCost(y, h, m)
    %assert logical(size(y) == size(h));
    dim = size(y);
    J = zeros(dim(1), dim(2));
    for ii = 1:dim(1)
        for jj = 1:dim(2)
            % size(1 / 2 / m * sum((y(ii,jj,:) - h(ii,jj,:)).^2))
            J(ii, jj) = 1 / 2 / m * sum((y(ii,jj,:) - h(ii,jj,:)).^2);
        end
    end
end

function y = linearEquation(a, b, x, dim)
    if (size(dim,2) ~= 2)
        error('Woops...');
    end
    [A,B] = meshgrid(a*ones(1,dim(1)), b*ones(1,dim(2)));
    y = zeros(dim(1), dim(2), length(x));
    for ii = 1:dim(1)
        for jj = 1:dim(2)
            for kk = 1:length(x)
                y(ii,jj,kk) = A(ii,jj) + B(ii,jj)*x(kk);
            end
        end
    end
end


function h = linearHypothesis(Theta0, Theta1, x)
    % Theta0 and Theta1 are supposed to be vectors
    % h will be a 3D matrix with Z axis representing different x values
    [T0, T1] = meshgrid(Theta0, Theta1);
    h = zeros(length(Theta0), length(Theta1), length(x));
    for ii = 1:length(Theta0)
        for jj = 1:length(Theta1)
            for kk = 1:length(x)
                h(ii,jj,kk) = T0(ii,jj) + T1(ii,jj)*x(kk);
            end
        end
    end
end

function fun(x)
    disp(x);
end