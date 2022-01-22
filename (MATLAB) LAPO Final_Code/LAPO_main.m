%___________________________________________________________________%
%  Lightning Attachment Procedure Optimization (LAPO) source codes demo version 1.0           %
%                                                                   %
%  Developed in MATLAB R2015b                                       %
%                                                                   %
%  Author and programmer: Amin Foroughi                             %
%         e-Mail: Amin.Forooghi @aut.ac.ir                          %
%                                                                   %
%   Main paper:Nematollahi, A. Foroughi, A. Rahiminejad, and B. Vahidi.%
%"A novel physical based meta-heuristic optimization method known as
%Lightning Attachment Procedure Optimization."                      %
%Applied Soft Computing 59 (2017): 596-621.                         %
%                                                                   %
%___________________________________________________________________%

% You can simply define your cost in a seperate file and load its handle to fobj
% The initial parameters that you need are:
%__________________________________________
% fobj = @YourCostFunction
% dim = number of your variables
% Max_iteration = maximum number of generations
% SearchAgents_no = number of search agents
% lb=[lb1,lb2,...,lbn] where lbn is the lower bound of variable n
% ub=[ub1,ub2,...,ubn] where ubn is the upper bound of variable n
% If all the variables have equal lower bound you can just
% define lb and ub as two single number numbers

% To run LAPO_main: [Best_score,Best_pos,cg_curve]=LAPO(SearchAgents_no,Max_iteration,lb,ub,dim,fobj)


clc
clear
close all
Function_name='F2'; % Name of the test function

SearchAgents_no=40; % Number of test point

Max_iteration=1000; % Maximum numbef of iterations

[lb,ub,dim,fobj]=Get_Functions_details(Function_name);

tic
[Best_score,Best_pos,cg_curve]=LAPO(SearchAgents_no,Max_iteration,lb,ub,dim,fobj);
toc

figure('Position',[500 500 660 290])
%Draw search space
% subplot(1,2,1);
% func_plot(Function_name);
% title('Test function')
% xlabel('x_1');
% ylabel('x_2');
% zlabel([Function_name,'( x_1 , x_2 )'])
% grid off

%Draw objective space
% subplot(1,2,2);
semilogy(cg_curve,'Color','r')
title('Convergence curve')
xlabel('Iteration');
ylabel('Best score obtained so far');

axis tight
grid off
box on
legend('LAPO')

display(['The best solution obtained by LAPO is : ', num2str(Best_pos)]);
display(['The best optimal value of the objective funciton found by LAPO is : ', num2str(Best_score)]);





