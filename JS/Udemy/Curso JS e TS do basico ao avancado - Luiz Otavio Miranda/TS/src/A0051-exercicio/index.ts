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
        }
    }
}
