from src.showtimes.usecase.movie_session.movie_session_extractor import MovieSessionExtractor
from src.showtimes.usecase.schedule.add_movie_session_to_schedule import AddMovieSessionToSchedule
from src.showtimes.usecase.schedule.add_movie_session_to_schedule_request import AddMovieSessionToScheduleRequest
from src.showtimes.usecase.schedule.schedule_extractor import ScheduleExtractor
from src.showtimes.usecase.schedule.schedule_persister import SchedulePersister


class AddMovieSessionToScheduleUseCase(AddMovieSessionToSchedule):
    __schedule_persister: SchedulePersister
    __schedule_extractor: ScheduleExtractor
    __movie_session_extractor: MovieSessionExtractor

    def __init__(
            self,
            schedule_persister: SchedulePersister,
            schedule_extractor: ScheduleExtractor,
            movie_session_extractor: MovieSessionExtractor
    ) -> None:
        self.__schedule_persister = schedule_persister
        self.__schedule_extractor = schedule_extractor
        self.__movie_session_extractor = movie_session_extractor

    def execute(self, request: AddMovieSessionToScheduleRequest) -> None:
        movie_session = self.__movie_session_extractor.get_by_id(request.movie_session_id)
        if movie_session is None:
            raise ValueError('Movie session not found.')

        schedule = self.__schedule_extractor.get_by_id(request.schedule_id)
        if schedule is None:
            raise ValueError('Schedule not found.')

        schedule.add_movie_session(movie_session)
        self.__schedule_persister.save(schedule)
