type VerifyUserFn = (user: User, receivedValue: User) => boolean;
type User = { username: string; password: string };

const verifyUser: VerifyUserFn = (user, receivedValue) => {
    return user.username === receivedValue.username && user.password === receivedValue.password;
};

const dbUser = {username: 'joao', password: '123456'}
const receivedUser = {username: 'joao', password: '123456', permissions: ''};
const loggedIn = verifyUser(dbUser, receivedUser);
