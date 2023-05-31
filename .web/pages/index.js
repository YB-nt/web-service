import { useEffect, useRef, useState } from "react"
import { useRouter } from "next/router"
import { connect, E, isTrue, preventDefault, refs, set_val, updateState, uploadFiles } from "/utils/state"
import "focus-visible/dist/focus-visible"
import { Button, Container, HStack, Input, Link, Text, useColorMode, VStack } from "@chakra-ui/react"
import { AtSignIcon, LockIcon } from "@chakra-ui/icons"
import NextLink from "next/link"
import NextHead from "next/head"


const PING = "http://localhost:8000/ping"
const EVENT = "ws://localhost:8000/event"
const UPLOAD = "http://localhost:8000/upload"

export default function Component() {
  const [state, setState] = useState({"box_height": "60px", "box_width": "60px", "id": "What's your email?", "id_check_opacity": "0%", "id_check_pos": "translate(5px, 0px)", "id_status": false, "id_underline": "0px solid white", "id_value": "", "id_width": "0px", "is_hydrated": false, "option": "JOB INFO", "pass_check_opacity": "0%", "pass_check_pos": "translate(5px, 0px)", "password": "Create a password.", "password_underline": "0px solid white", "password_width": "0px", "pwd_status": false, "pwd_value": "", "result_color": "", "result_opacity": "0%", "result_pos": "transform(0px, 0px)", "result_sign_in": "", "resutl_stauts": "text", "events": [{"name": "state.hydrate"}], "files": []})
  const [result, setResult] = useState({"state": null, "events": [], "processing": false})
  const router = useRouter()
  const socket = useRef(null)
  const { isReady } = router
  const { colorMode, toggleColorMode } = useColorMode()

  const Event = (events, _e) => {
      preventDefault(_e);
      setState({
        ...state,
        events: [...state.events, ...events],
      })
  }

  const File = files => setState({
    ...state,
    files,
  })

  useEffect(()=>{
    if(!isReady) {
      return;
    }
    if (!socket.current) {
      connect(socket, state, setState, result, setResult, router, EVENT, ['websocket', 'polling'])
    }
    const update = async () => {
      if (result.state != null){
        setState({
          ...result.state,
          events: [...state.events, ...result.events],
        })

        setResult({
          state: null,
          events: [],
          processing: false,
        })
      }

      await updateState(state, setState, result, setResult, router, socket.current)
    }
    update()
  })
  useEffect(() => {
    const change_complete = () => Event([E('state.hydrate', {})])
    router.events.on('routeChangeComplete', change_complete)
    return () => {
      router.events.off('routeChangeComplete', change_complete)
    }
  }, [router])


  return (
    <Container centerContent={true} sx={{"justifyContent": "center", "maxWidth": "auto", "height": "100vh", "bg": "#1D2330"}}>
  <Container centerContent={true} sx={{"width": "400px", "height": "75vh", "bg": "#1D2330", "boxShadow": "41px -41px 82px #0d0f15,-41px 41px 82px #2d374b", "borderRadius": "15px"}}>
  <VStack>
  <Container sx={{"height": "65px"}}/>
  <Container centerContent={true} sx={{"width": "250px"}}>
  <Text sx={{"fontSize": "28px", "color": "white", "fontWeight": "bold", "letterSpacing": "2px"}}>
  {`Sign In`}
</Text>
</Container>
  <Container centerContent={true} sx={{"width": "250px"}}>
  <Text sx={{"fontSize": "12px", "color": "white", "fontWeight": "#eeeeee", "letterSpacing": "0.2px"}}>
  {`Search For Skill Information By Job`}
</Text>
</Container>
  <Container sx={{"height": "50px"}}/>
  <Container sx={{"borderBottom": "0.1px solid grey", "width": "300px", "height": "45px"}}>
  <HStack>
  <AtSignIcon sx={{"color": "white", "fontSize": "11px"}}/>
  <Input focusBorderColor="None" placeholder="Username" sx={{"border": "0px", "color": "white", "fontWeight": "semibold", "fontSize": "11px"}} type=""/>
</HStack>
</Container>
  <Container sx={{"height": "5px"}}/>
  <Container sx={{"borderBottom": "0.1px solid grey", "width": "300px", "height": "45px"}}>
  <HStack>
  <LockIcon sx={{"color": "white", "fontSize": "11px"}}/>
  <Input focusBorderColor="None" placeholder="Password" sx={{"border": "0px", "color": "white", "fontWeight": "semibold", "fontSize": "11px"}} type="password"/>
</HStack>
</Container>
  <Container sx={{"height": "5px"}}/>
  <Container sx={{"width": "300px", "height": "45px"}}>
  <Text sx={{"color": "white", "fontSize": "11px", "textAlign": "end"}}>
  <NextLink href="/signup" passHref={true}>
  <Link as="span">
  {`Sign Up`}
</Link>
</NextLink>
</Text>
</Container>
  <Container sx={{"height": "45px"}}/>
  <Container>
  <Button sx={{"width": "300px", "height": "45px"}}>
  <Text sx={{"color": "white", "fontSize": "13px", "weight": "bold"}}>
  {`Sign In`}
</Text>
</Button>
</Container>
</VStack>
</Container>
  <NextHead>
  <title>
  {`Login Page`}
</title>
  <meta content="A Pynecone app." name="description"/>
  <meta content="favicon.ico" property="og:image"/>
</NextHead>
</Container>
  )
}
