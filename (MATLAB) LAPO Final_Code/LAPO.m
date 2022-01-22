function [Best_score,Best_pos,cg_curve]=LAPO(SearchAgents_no,Max_iteration,lb,ub,dim,fobj)
if size(ub,2)==1
    Ub=ones(1,dim).*ub;
    ub=Ub;
end
if size(lb,2)==1
    Lb=ones(1,dim).*lb;
    lb=Lb;
end
xold=initialization(SearchAgents_no,dim,ub,lb)';
ng=SearchAgents_no;
tmax=Max_iteration;
nv=dim;
xav=mean(xold,1);
fav=fobj(xav);
for i=1:SearchAgents_no
    fold(i,1)=fobj(xold(i,:));
end
for t=1:Max_iteration
    %% Phase 1
    [a,b]=sort(fold);
    if fav<(fold(b(ng,1),1))
        fold(b(ng,1),1)=(fav);
        xold(b(ng,1),:)=xav;
    end
    [a,b]=sort(fold);
    xav=mean(xold,1);
    fav=fobj(xav);
    for r=1:ng
        u=randperm(ng);
        if fav<fold(u(r))
            for i=1:nv
                xnew(r,i)=xold(r,i)+rand*(+xav(1,i)-rand*xold(u(r),i));
                if  xnew(r,i)>ub(1,i)
                    xnew(r,i)=ub(1,i);
                end
                if  xnew(r,i)<lb(1,i)
                    xnew(r,i)=lb(1,i);
                end
                
            end
            %          xnew(r,2)=xold(r,2)+rand*(+xav1(1,2)-rand*xold(u(r),2));
        else
            for i=1:nv
                xnew(r,i)=xold(r,i)-rand*(+xav(1,i)-rand*xold(u(r),i));
                % cheak uper and lower band
                if  xnew(r,i)>ub(1,i)
                    xnew(r,i)=ub(1,i);
                end
                if  xnew(r,i)<lb(1,i)
                    xnew(r,i)=lb(1,i);
                end
            end
            %          xnew(r,2)=xold(r,2)-rand*(+xav1(1,2)-rand*xold(u(r),2));
        end
        %% better result
        fnew(r,:)=fobj(xnew(r,:));
        if fnew(r,:)>fold(r,:)
            fnew(r,:)=fold(r,:);
            xnew(r,:)=xold(r,:);
        end
    end
    %% Phase 2
    fold=fnew;
    xold=xnew;
    [a,b]=sort(fold);
    
    for r=1:ng
        for i=1:nv
            yu=1-(t*1/tmax)*exp(-(t^1)/tmax);
            y=(+yu*(xold(b(ng,1),i)-xold(b(1,1),i)));
            xnew(r,i)=xold(r,i)-rand*y;
            % cheak uper and lower band
            if  xnew(r,i)>ub(1,i)
                xnew(r,i)=ub(1,i);
            end
            if  xnew(r,i)<lb(1,i)
                xnew(r,i)=lb(1,i);
            end
        end
        fnew(r,1)=fobj(xnew(r,:));
        %% better result
        if fnew(r,:)>fold(r,:)
            fnew(r,:)=fold(r,:);
            xnew(r,:)=xold(r,:);
        end
    end
    
    fold=fnew;
    xold=xnew;
    [a,b]=sort(fold);
    cg_curve(t)=a(1,1);

    display(['At iteration ', num2str(t), ' the elite fitness is ', num2str(a(1,1))]);
end
Best_pos=xold(b(1,1),:);
Best_score=a(1,1);

end