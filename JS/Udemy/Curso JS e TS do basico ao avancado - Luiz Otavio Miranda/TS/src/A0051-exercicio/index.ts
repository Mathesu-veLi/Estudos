type VoteOption = {
    numberOfVotes: number;
    option: string;
};

export class Voting {
    private _voteOption: VoteOption[] = [];
    constructor(public details: string) {}

    addVoteOption(voteOption: VoteOption): void {
        this._voteOption.push(voteOption);
    }

    vote(votingIndex: number): void {
        if (!this._voteOption[votingIndex]) return;
        this._voteOption[votingIndex].numberOfVotes++;
    }

    get voteOption(): VoteOption[] {
        return this._voteOption;
    }
}

export class VotingApp {
    private votes: Voting[] = [];

    addVote(votingIndex: Voting): void {
        this.votes.push(votingIndex);
    }

    showVotes(): void {
        for (const vote of this.votes) {
            console.log(vote.details);
            for (const voteOption of vote.voteOption) {
                console.log(voteOption.option, voteOption.numberOfVotes);
            }
            console.log('###');
            console.log('');
        }
    }
}

const voting1 = new Voting('Qual sua linguagem de programação favorita?');

voting1.addVoteOption({ option: 'Python', numberOfVotes: 0 });
voting1.addVoteOption({ option: 'JavaScript', numberOfVotes: 0 });
voting1.addVoteOption({ option: 'TypeScript', numberOfVotes: 0 });
voting1.vote(1);
voting1.vote(1);
voting1.vote(0);
voting1.vote(0);
voting1.vote(0);
voting1.vote(0);
voting1.vote(2);

const votingApp = new VotingApp();
votingApp.addVote(voting1);
votingApp.showVotes();
