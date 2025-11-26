import {Route, Routes} from 'react-router';

import './app.css';
import {AuthPage} from './pages/auth-page';
import {HomePage} from './pages/home-page';
import {NotFoundPage} from './pages/not-found-page';
import {ThreadPage} from './pages/thread-page';

export const App = function () {
    return (
        <Routes>
            <Route path="/auth" element={<AuthPage />} />
            <Route path="/" element={<HomePage />} />
            <Route path="/thread/:thread_id" element={<ThreadPage />} />
            <Route path="*" element={<NotFoundPage />} />
        </Routes>
    );
};
