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

    addVoting(votingIndex: Voting): void {
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

const voting2 = new Voting('Qual sua cor favorita?');

voting2.addVoteOption({ option: 'Vermelho', numberOfVotes: 0 });
voting2.addVoteOption({ option: 'Verde', numberOfVotes: 0 });
voting2.addVoteOption({ option: 'Azul', numberOfVotes: 0 });
voting2.vote(1);
voting2.vote(1);
voting2.vote(1);
voting2.vote(2);
voting2.vote(2);
voting2.vote(2);
voting2.vote(0);

const votingApp = new VotingApp();
votingApp.addVoting(voting1);
votingApp.addVoting(voting2);
votingApp.showVotes();
