import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

if __name__ == "__main__":
    plt.rc('xtick', labelsize=14)
    plt.rc('ytick', labelsize=14)
    plt.rc('legend', fontsize=14)

    price_list = np.load('Results/price_list.npy')

    ax = sns.lineplot(data=price_list)
    ax.set_xticklabels(labels=[])
    ax.set_yticklabels(labels=[])

    m1_shortfall_list = np.load('Results/1e-6_shortfall_list.npy')
    m03_shortfall_list = np.load('Results/1e-6_shortfall_list_0.3M.npy')
    m07_shortfall_list = np.load('Results/1e-6_shortfall_list_0.7M.npy')

    E1_list = []
    E2_list = []
    B1_list = []
    B2_list = []
    for i in range(len(m1_shortfall_list)):
        E1_list.append(m1_shortfall_list[i])
        E2_list.append(m03_shortfall_list[i] + m07_shortfall_list[i])
        B1_list.append(m03_shortfall_list[i])
        B2_list.append(m07_shortfall_list[i])

    T = np.arange(1, 101).tolist()

    df1 = pd.DataFrame()
    # df1['Time'] = T
    df1['Agent A'] = E1_list
    df1['B1+B2'] = E2_list
    df1['Agent B1'] = B1_list
    df1['Agent B2'] = B2_list

    sns.set()

    ax = sns.lineplot(data=df1)
    ax.set_ylabel('Expected Shortfall', fontsize=20)
    ax.set_xlabel('Episodes ', fontsize=20)
    ax.set_xticklabels([0, 0, 2000, 4000, 6000, 8000, 10000], fontsize=14)
    ax.grid(b=True, which='major', color='black', linewidth=0.5, linestyle='--')
    plt.show()

    A1 = np.load('Results/1e-4_optimal.npy')
    A2 = np.load('Results/1e-9_optimal.npy')
    B = np.load('Results/1e-4_1e-9_trajectory.npy')

    A1_list = []
    A2_list = []
    B1_list = []
    B2_list = []
    for i in range(len(A1)):
        A1_list.append(A1[i])
        A2_list.append(A2[i])
        B1_list.append(B[i][0])
        B2_list.append(B[i][1])

    df2 = pd.DataFrame()
    # df1['Time'] = T
    df2['Agent A1'] = A1_list
    df2['Agent A2'] = A2_list
    df2['Agent B1'] = B1_list
    df2['Agent B2'] = B2_list

    ax = sns.lineplot(data=df2)
    ax.set_ylabel('Percentage', fontsize=20)
    ax.set_xlabel('Time (Day)', fontsize=20)
    ax.set_xticklabels([0, 0, 10, 20, 30, 40, 50, 60], fontsize=14)
    ax.grid(b=True, which='major', color='black', linewidth=0.5, linestyle='--')
    plt.show()

    # Co-operation and Competition
    A = np.load('Results/1e-6_shortfall_list.npy')
    B = np.load('Results/1e-6_1e-6_competition_shortfall_list.npy')
    C = np.load('Results/1e-6_1e-6_cooporation_shortfall_list.npy')

    A_list = []
    B_list = []
    C_list = []
    for i in range(len(A)):
        A_list.append(A[i])
        B_list.append(B[i].sum())
        C_list.append(C[i].sum())

    df3 = pd.DataFrame()
    df3['Independent'] = A_list
    df3['Competitive'] = B_list
    df3['Cooporative'] = C_list

    ax = sns.lineplot(data=df3)
    ax.set_ylabel('Expected Shortfall', fontsize=20)
    ax.set_xlabel('Episodes', fontsize=20)
    ax.set_xticklabels([0, 0, 2000, 4000, 6000, 8000, 10000], fontsize=14)
    ax.grid(b=True, which='major', color='black', linewidth=0.5, linestyle='--')
    plt.show()

    # Competitor Selling Fixed Amount
    A = np.load('Results/1e-6_optimal.npy')
    B = np.load('Results/1e-6_trajectory_fixed_competitor.npy')

    B = np.zeros(61)
    B[0:2] = np.load('Results/1e-6_trajectory_fixed_competitor.npy')

    A_list = []
    B_list = []
    for i in range(len(A)):
        A_list.append(A[i])
        B_list.append(B[i])

    df4 = pd.DataFrame()
    df4['Independent'] = A_list
    df4['With Competitor'] = B_list

    ax = sns.lineplot(data=df4)
    ax.set_ylabel('Expected Shortfall', fontsize=20)
    ax.set_xlabel('Time (Day)', fontsize=20)
    ax.grid(b=True, which='major', color='black', linewidth=0.5, linestyle='--')
    plt.show()
