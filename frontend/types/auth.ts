export type LoginCredentials = {
  email: string;
  password: string;
};

export type AuthToken = {
  access_token: string;
  token_type: "bearer";
};

export type AuthState = {
  token: string | null;
  isAuthenticated: boolean;
  isLoading: boolean;
};
