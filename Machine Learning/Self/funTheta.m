% Theta0 = -5:0.1:5;
Theta1 = -5:0.1:5;

a = 0;
b = 1;

x = -5:0.5:5;
y = a + b*x;

% [T0, T1] = meshgrid(Theta0, Theta1);

% h(T) = T0 + T1*x
% J(T) = 1/2m * sum(h - y)
J = zeros(size(Theta1));
for i = 1:length(Theta1)
    J(i) = 1/2/length(x)*sum((Theta1(i)*x - y).^2);
end